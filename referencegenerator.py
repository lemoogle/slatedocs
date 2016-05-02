import requests
from mako.template import Template
from mako.lookup import TemplateLookup
from bunch import Bunch
mytemplate = Template(filename='referencetemplate.template')


apikey = ""
discoveryurl="http://api.idolondemand.com/1/discovery/api?apikey="+apikey+"&max_results=1000&full_definition=true"
testurl="http://api.idolondemand.com/1/discovery/api?apikey="+apikey+"&full_definition=true&search_text=sentiment"
resp=requests.get(discoveryurl)
apilist = resp.json()
specialparams=["text","file","reference","url","json","index_reference"]
for api in apilist:
    newparams=[]
    inputs=[]
    enums=[]
    for (name,val) in api["parameters"]["schema"]["properties"].items():
        param = val
        param["name"]=name
        param["required"]=name in api["parameters"]["schema"].get("required",[])
        if "description" not in param:
            param["description"]=""
        if "items" in val and 'enum_documentation' in val["items"]:
            #print val["items"]
            val["enum_documentation"]=val["items"]["enum_documentation"]
        if "enum" in val:
            for enum in val["enum_documentation"]:
                val["enum_documentation"][enum]["name"]=enum
                val["enum_documentation"][enum]["default"]= enum in val.get("default",[])
            enum= {"name":name,"vals":val["enum_documentation"].values()}
            enums.append(enum)
        if name in specialparams:
            inputs.append(name)
        else:
            newparams.append(param)
    api["params"]=newparams
    api["inputs"]=inputs
    api["enums"]=enums

    api.pop("response")
    api.pop("parameters")
bunch=Bunch.fromDict(apilist)
print(mytemplate.render(data=bunch))
