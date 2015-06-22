### Getting Set Up
 1. **Bundler** — If Ruby is already installed, but the `bundle` command doesn't work, just run `gem install bundler` in a terminal.
 4. Install all dependencies: `bundle install`
 5. Start the test server: `bundle exec middleman server`

Or use the included Dockerfile! (must install Docker first)

```shell
docker build -t slate .
docker run -d -p 4567:4567 slate
```
You can now see the docs at <http://localhost:4567>. Whoa! That was fast!

*Note: if you're using the Docker setup on OSX, the docs will be
availalable at the output of `boot2docker ip` instead of `localhost:4567`.*


## Editing the docs

Read about Slate Markdown [editing Slate markdown](https://github.com/tripit/slate/wiki/Markdown-Syntax).


### Add a new Section

* Create a new file `\_sectionname.md` in the includes folder

### Easy API calls sample code

* Name your includes file `.md.erb` instead of `.md`
