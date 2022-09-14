// cleanAMZLink

const run = () => {
    let args, exit, out
    if (typeof Deno == 'undefined') {
        const process = require('process')
        args = process.argv.slice(2)
        exit = process.exit
        out = async (input) => {
            await process.stdout.write(input)
        }
    } else {
        args = Deno.args
        exit = Deno.exit
        out = async (input) => {
            await Deno.stdout.write(new TextEncoder().encode(input))
        }
    }
    const re = new RegExp(/(amazon[\w\.]+)\/([^\$\n]+)?dp\/([\w]+)/)
    const match = re.exec(args[0])
    if (match) {
        out(`https://www.${match[1]}/dp/${match[3]}`)
    } else {
        exit(1)
    }
}

run()
