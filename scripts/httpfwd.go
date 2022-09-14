package main

import (
	"context"
	"flag"
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"net/http"
	"regexp"
)

func OverwriteHeader(w http.ResponseWriter, h http.Header) {
	for name, headers := range h {
		for _, hdr := range headers {
			w.Header().Set(name, hdr)
		}
	}

}

func CfHandleFunc(service string, reqpath string, w http.ResponseWriter, req *http.Request) {
	host := fmt.Sprintf("%s.mamoru.workers.dev", service)
	newURL := fmt.Sprintf("https://%s%s", host, reqpath)

	ctx := context.Background()
	newReq := req.Clone(ctx)
	newReq.Host = host
	parsedURL, _ := newReq.URL.Parse(newURL)
	newReq.URL = parsedURL
	newReq.RequestURI = ""

	client := &http.Client{}
	resp, err := client.Do(newReq)
	if err != nil {
		panic(err)
	}

	res, err := ioutil.ReadAll(resp.Body)
	if err != nil && err != io.EOF {
		panic(err)
	}

	OverwriteHeader(w, resp.Header)
	w.WriteHeader(resp.StatusCode)
	w.Write(res)
}

func route(w http.ResponseWriter, req *http.Request) {
	rCf := regexp.MustCompile(`^/cf/([^\/|\?]+)([^$]*)`)
	switch {
	case rCf.MatchString(req.URL.Path):
		log.Printf("got request from %s, requesting %s", req.RemoteAddr, req.URL.String())
		groups := rCf.FindStringSubmatch(req.URL.String())
		CfHandleFunc(groups[1], groups[2], w, req)
	default:
		w.WriteHeader(http.StatusBadRequest)
		w.Write([]byte(fmt.Sprintf("Unknown route: %s\n", req.URL.Path)))
	}
}

func main() {
	port := flag.Int("port", 80, "port number")
	cert := flag.String("cert", "", "cert file")
	pvk := flag.String("pvk", "", "private key file")
	flag.Parse()
	port_str := fmt.Sprintf(":%d", *port)

	http.HandleFunc("/", route)
	if len(*cert) > 0 && len(*pvk) > 0 {
		fmt.Printf("Listening on %s with TLS\n", port_str)
		err := http.ListenAndServeTLS(port_str, *cert, *pvk, nil)
		if err != nil {
			panic(err)
		}
	} else {
		fmt.Printf("Listening on %s without TLS\n", port_str)
		err := http.ListenAndServe(port_str, nil)
		if err != nil {
			panic(err)
		}
	}
}
