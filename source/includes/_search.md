# Guide - Indexing

Text Indexes in IDOL OnDemand allow the indexing of documents, files, tweets or any other form of unstructured text content. Once indexed that content can be searched through utilizing IDOL's powerful conceptual search capabilities; not only can the content be searched it can be organized, categorized, clustered and linked.

## Getting Started with Indexing

### Create a Text Index

Before indexing documents, we must first create a Text Index.

We will need to specify:
* An index name
* An index flavor : flavors are preconfigurations for our indexes, specifying a starting schema and a document limit.

```shell
curl -X POST -F index=myindex -F apikey= xxXXXXxXxxxXXXXXxxxXXXXXxxxxxx  https://api.idolondemand.com/1/api/sync/createtextindex/v1
```

### Adding documents to an index

After we create an index, we can start populating it with data.
To do so we use the [Add to Text Index API]().
The Add to Text Index API supports two types of inputs:
* files: IDOL OnDemand will automatically extract content and metadata for over 500 file types and index the data. These files can be provided via url or posted to the api directly
* json: Like a NoSQL database, IDOL OnDemand indexes can index JSON documents.

#### JSON documents

> Required format for json input

```json
{
   "document" :
   [
      {
         "title" : "This is my document",
         "reference" : "mydoc1",
         "myfield" : ["a value"],
         "content" : "A large block of text, which makes up the main body of the document."
      }, {
         "title" : "My Other document",
         "reference" : "mydoc2",
         "content" : "This document is about something else"
      }
   ]
}
```
While the json document format allows any field the following fields are worth noting:

* title and content : these fields are indexed for conceptual retrieval and relation linking.
* reference: automatically generated if not present, consider this the unique id of the documents indexed


```shell
curl -X POST  -F json='{"document" :[{"title" : "This is my document","reference" : "mydoc1","myfield" : ["a value"],"content" : "A large block of text, which makes up the main body of the document."}]}' -F index= myindex -F apikey= xxXXXXxXxxxXXXXXxxxXXXXXxxxxxx "https://api.idolondemand.com/1/api/sync/addtotextindex/v1"
```

#### Files

The API will extract text and metadata from files

```shell
curl –X POST -F file=@/home/user/testdata/sample.doc -F index= myindex -F apikey= xxXXXXxXxxxXXXXXxxxXXXXXxxxxxx "https://api.idolondemand.com/1/api/sync/addtotextindex/v1"

curl –X POST -F url=http://example/example.doc -F index= myindex -F apikey= xxXXXXxXxxxXXXXXxxxXXXXXxxxxxx "https://api.idolondemand.com/1/api/sync/addtotextindex/v1"
```

### Querying a Text Index

After you populate your index, you can perform searches to get detailed information about your data. The `Query Text Index` API allows you to perform text searches on your index.

```shell
curl –X POST -F text= myquery -F indexes= myindex -F apikey= xxXXXXxXxxxXXXXXxxxXXXXXxxxxxx -F "https://api.idolondemand.com/1/api/sync/querytextindex/v1"
```

## Field Types

Data in the IDOL OnDemand text index is stored in fields. The fields can have different types depending on the content of the field, and what the field is used for. This page describes the main field types and their uses.

Field | Description
---- | ---
Reference | The Reference fields contain a document reference that identifies the document. This might be a file path or URL, or some other identifying content. You can use this field to retrieve a specific document.
Index | Index fields contain the majority of the document content. When the data is indexed, index fields receive additional processing, such as stemming and stop word removal, to make it easier to search the data. Typically, index fields contain text that you query frequently, such as the title and main body of a document. You can also use Query Text field restrictions for Index fields. See Field Restrictions.
Parametric| Parametric fields contain content for parametric (faceted) search and filtering.  Typically, it contains a limited set of values to make it easier to filter content by a value. You can also use the MATCH FieldText operator for Parametric fields.  See FieldText Operators.
Numeric| Numeric fields contain a number.  This field type makes it faster to search for specific numeric values, and also enables searching for ranges, or values near a specified number, by using numeric FieldText operators.  See FieldText Operators.
Date| Date fields contain a date, in one of the configured date formats.  This field type makes it faster to search for dates, and enables searching for date ranges, or dates near a specified date, by using the date FieldText Operators.  See FieldText Operators.
Rank| Rank fields contain an internal document rank, which you can use to order search results.  Rank values are also used to bias the relevance sort order.
Store Only| Store Only fields contain any other type of data that does not have a special type.  These fields generally contain values that you do not need to search for specifically, but which might be useful information, such as the content length.

## Flavors
Flavor | Description
---- | ----
Querymanipulation| An query manipulation index is used to store promotions and other query promotions to be applied as part of a query profile.
Custom_Fields| A custom_field configuration that can accept up to 250,000 documents.
Explorer Flavor| An explorer configuration that can accept up to 25,000 documents.
Standard| A standard configuration that can accept up to 250,000 documents.
Categorization| An categorization index is used to categorise documents based on boolean restrictions and can be used to define up to 250,000 categories.
