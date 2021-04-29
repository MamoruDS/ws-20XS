const OPT = {
    // owner: 'owner id',
    target: 'chat id',
    token: 'your bot token',
}

// global variable SMSRF as sender
// global variable SMSRB as message content
const LOC = {
    smsFrom: global('%SMSRF') || 'unknown sender',
    smsBody: global('%SMSRB') || 'empty message',
}

const safeMDv2 = (input) => {
    return input.replace(
        /(?<!\\)[\_\*\[\]\(\)\~\`\>\#\+\-\=\|\{\}\.\!]/gm,
        (match, ...M) => {
            return '\\' + match
        }
    )
}

const safeTag = (input, nonMD) => {
    input = input.replace(/[\ |\.|\-|\|:|：]/gm, '_')
    input = input.replace(/[\uff00-\uffff|\u0000-\u00ff]/g, (m) => {
        return /\w/.exec(m) == null ? '' : m
    })
    const output = '#' + input
    return nonMD ? output : safeMDv2(output)
}

const formatSMS = (sender, body) => {
    let alias = undefined
    const _sender = safeMDv2(sender)
    const _body = safeMDv2(body).replace(/[【|\[](.{1,})[】|\]]/gm, (...M) => {
        alias = safeTag(M[1], false)
        return ''
    })
    const re = new RegExp(/\d{4,}/gm)
    const codes = _body.match(re)
    const url = `https://mamoruds.github.io/redir_page/?redir=${encodeURIComponent(
        `sms://${_sender}`
    )}`
    return `*\\[ \\#SMS \\]* [📮](${url}) ${alias ? `${alias}` : `\`${_sender}\``
        }\n${_body}${codes
            ? `\n\n${codes
                .map((code) => {
                    return `\`${code}\``
                })
                .join(', ')}`
            : ''
        }`
}

const fwd = (text) => {
    const xhr = new XMLHttpRequest()
    const data = new FormData()
    data.append('chat_id', OPT.target)
    data.append('text', text)
    data.append('parse_mode', 'MarkdownV2')
    xhr.open('POST', `https://api.telegram.org/bot${OPT.token}/sendMessage`)
    xhr.onload = function () {
        exit()
    }
    xhr.send(data)
}

fwd(formatSMS(LOC.smsFrom, LOC.smsBody))
