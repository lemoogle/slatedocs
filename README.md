# Slate documents for IDOL OnDemand

THis is a documentation based on the Slate project, a framework for Documentation. Find out more about it on its [Github Repo](https://github.com/tripit/slate)


## Haven OnDemand Docs Generation


### API Reference generation

Two files handle the generation 

* **referencegenerator.py** : The python script that will call the API discovery API from idolondemand to generate the API reference
* **referencetemplate.template** : The Mako template that generates the API reference. 

To run the generation .

Set your APIKEY in the referencegenerator.py file.

Then run

```shell
python referencegenerator.py > source/includes/_reference.md
```


### Adding Manual Documentation 

Edit index.md to add new documentation files. Add an entry to the includes section, these are in order.

```
includes:
  - auth
  - asyncsync
  - files
  - errors
  - libraries
  - guides
  - reference
```

Every include matches a file in the includes directory with the name _auth.md or _reference.md
You can also use _name.md.erb when using automated code samples (see below)

For guides, edit guides/index.md and do the same thing. Guides are accessible at `/guides`


### Automated code samples

**codesnippets/_codetemplates.md.erb** : is an ERB template that will generate the code samples for all 4 languages configured currently ( shell, javascript, python and ruby)


To create code samples name your content file _name.md.erb and add the following:

```erb
<%= partial(:'codesnippets/codetemplates',
:locals => {:api => "createconnector", :sync=>"sync", :method=>"POST",
  :params=>{"connector"=>"idolondemand", "flavor"=>"web_cloud", "config"=>'{ "url" : "http://www.idolondemand.com" }',"destination"=>'{ "action" : "addtotextindex", "index" : "iodsite" }' }} ) %>
```

This will generate code samples to call the createconnector api , sync calls doing POST.


## Slate - Setup and deployment

### Running/Building the docs
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



Slate spits out a bunch of static HTML, Javascript, and CSS, so it's pretty trivial to host.

### Publishing Your Docs to Github Pages

Publishing your API documentation couldn't be more simple.

 1. Commit your changes to the markdown source: `git commit -a -m "Update index.md"`
 2. Push the *markdown source* changes to Github: `git push`
 3. Add "gh-pages" as a local branch pointing to the remote ([GitHub doc](https://help.github.com/articles/creating-project-pages-manually))
 4. Compile to HTML, and push the HTML to Github pages: `rake publish`

Done! Your changes should now be live on http://yourusername.github.io/slate, and the main branch should be updated with your edited markdown. Note that if this is your first time publishing Slate, it can sometimes take ten minutes or so before your content is available online.

### Publishing Your Docs to Your Own Server

Instead of using `rake publish`, use `rake build`. Middleman will build your website to the `build` directory of your project, and you can copy those static HTML files to the server of your choice.

Another alternative is to use the [middleman-deploy](https://github.com/middleman-contrib/middleman-deploy) gem. 

### Custom Domains with Github

If you're hosting Slate with Github Pages, setting up a custom domain name is simple! Just follow the instructions [in Github's help center](https://help.github.com/articles/setting-up-a-custom-domain-with-github-pages/). Note that instead of putting the `CNAME` file in the root directory of your Slate, you should put it in the `source` folder. When Middleman publishes to the `gh-pages` branch, it will copy it to the root folder of that branch.

## Editing the docs

Read about Slate Markdown [editing Slate markdown](https://github.com/tripit/slate/wiki/Markdown-Syntax).


### Add a new Section

* Create a new file `\_sectionname.md` in the includes folder

### Easy API calls sample code

* Name your includes file `.md.erb` instead of `.md`
