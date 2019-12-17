# Demo Postman importing OpenAPI as a collection

We publish OpenAPI specs to help developers explore and integrate with our APIs better. Here's a quick example using Postman.

(Download Postman from https://getpostman.com)

**Get the OAS**

Go to https://developer.nexmo.com/api and choose which spec you want. There should be a "Download this OpenAPI 3 Specification" button so click to download a yaml file.

**Import into Postman**

Open Postman, and choose "Import" at the top of the left hand bar (right at the top, above the filter/search box).

On the "Import File" tab, do "Choose Files" and navigate to the OAS you just downloaded.

Once it has imported you will see a new collection folder in the left hand bar with a name like "Nexmo Account API" - expand it and there will be a series of ready-configured requests for all the documented endpoints of the API.

Click on one of the requests and it will load into the main (right hand) pane. This allows you to add your API key and secret, and whatever else makes sense, and click "send". You may need to scroll down to see the response.
