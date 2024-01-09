const http = require('http')
const path = require('path')
const { I18n } = require('i18n')

const i18n = new I18n({
  directory: path.join(__dirname, './locales'),
  locales: ['en_US', 'zh_CN'],
  defaultLocale: 'en_US'
});

const app = http.createServer((req, res) => {
  i18n.init(req, res)
  res.end(res.__('hello_nazu'))
});

app.listen(3000, '127.0.0.1');