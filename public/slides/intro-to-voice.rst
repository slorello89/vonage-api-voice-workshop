.. footer::

    #VonageCampus ~ @lornajane

Getting Started with Voice API
##############################

.. class:: titleslideinfo

    Lorna Mitchell, Developer Relations

.. Change to a standard page
.. raw:: pdf

    PageBreak standardPage

Getting Started with Voice API
==============================

Use the Voice API to make and receive calls, play audio, send and
receive DTMF tones, and to record calls.

|

Workshop plan:

* Introduce concepts and vocabulary (mostly talking)
* Make and receive calls (hands-on)
* Interact with user input (hands-on)

.. raw:: pdf

    TextAnnotation "A bit of talking, then three exercises for you to try. Use the time well, we're here to help and we'd love to show you around!"

    TextAnnotation "First up: the abbreviation you're going to hear the most today!"

.. Change to a title page
.. raw:: pdf

    PageBreak titlePage

NCCO
====

.. Change to a standard page
.. raw:: pdf

    PageBreak standardPage

NCCO: Nexmo Call Control Object
===============================

A series of steps: e.g. text-to-speech

.. code:: json

  [
    {
      "action": "talk",
      "text": "You are listening to a Call made with Voice API"
    }
  ]

|

You can find a full reference here: https://developer.nexmo.com/voice/voice-api/ncco-reference

.. raw:: pdf

    TextAnnotation "NCCOs describe the flow of the call. They are a series of steps described in JSON"

    TextAnnotation "NCCOs can contain multiple objects in the array, they are done in order and then the call ends when there are no more"

    TextAnnotation "DEMO: Open the NCCO reference page from developer.nexmo.com to encourage people"

    TextAnnotation "Examples are on the next slide, feel free to name drop audio, DTMF input, recording ... but don't go mad"


NCCO: Nexmo Call Control Object
===============================

Elements in an NCCO may include:

- text-to-speech
- playing audio (optionally looping)
- recording a call
- accepting DTMF input
- transferring a call (to a conversation, or a new NCCO)
- ... and much more

.. raw:: pdf

  TextAnnotation "Emphasise that these are really important at every stage of voice call applications!"

  TextAnnotation "Recordings: start the recording, include a recording_url. When complete, webhook goes to recording_url with a URL you can download if you are signed in (there are examples in today's exercises)."

  TextAnnotation "Audio should be hosted on a public URL, such as S3"

  TextAnnotation "DTMF you ask for input, and give the URL to send info to. That URL (synchronously) returns a new NCCO in response to the given data."

  TextAnnotation "Call vs Conferences is the next slide"

Calls vs Conferences
====================

There are two types of conversation that you might use:

- A "call" is a temporary conversation that only exists for as long as the call is taking place

- A "conference" is a conversation with a name, that additional callers can be added to. This type of conversation persists and can be reused.

|

.. code:: json

    {
      "action": "conversation",
      "name": "nexmo-conference-standard",
      "record": "true"
    }


.. raw:: pdf

  TextAnnotation "Today's examples only use calls"

  TextAnnotation "Use a Conference when you need to know which conversation to have new users join, e.g. conference call or an outgoing call to connect to an existing call when it is answered"

.. Change to a title page
.. raw:: pdf

    PageBreak titlePage

Nexmo Voice API
===============

.. Change to a standard page
.. raw:: pdf

    PageBreak standardPage

Nexmo Voice API
===============

Make an API call to:

* make an outgoing call (we'll do this in a bit)
* hang up a call
* transfer a call
* interact with an in-progress call
* get information about current and past calls

.. raw:: pdf

  TextAnnotation "Make the distinction between the NCCO (supplied when the call is started/answered) and the API which operates on the in-progress call and can change things even during the course of an NCCO."

The Voice API
=============

The Voice API is an HTTP API so you can access it in many different ways:

* Explore the API with Postman or your favorite HTTP client
* Use ``request(s)`` or whichever library you prefer in your application
* Try one of our Server SDKS: https://developer.nexmo.com/tools (recommended)

|

You will find lots of code examples and the API reference on https://developer.nexmo.com

.. raw:: pdf

  TextAnnotation "Really recommend our server SDKs, they make things easier. Available for Java, .NET, Python, NodeJS, PHP, Ruby and Golang."

  TextAnnotation "Code samples on Nexmo Developer have cURL as well so if you're not using a lib, check those"

  TextAnnotation "For exploring the APIs, grab the OpenAPI spec and import into Postman. This makes a great demo if you have postman installed! Download the OAS, go to 'import' above collections, import file, choose your file, and you get a new collection"

.. Change to a title page
.. raw:: pdf

    PageBreak titlePage

NCCO + API = Many Good Things
=============================


.. raw:: pdf

    TextAnnotation "Combining the NCCOs to control program flow and the API calls to react to events allows us to create interesting and fully-featured applications."
  TextAnnotation "Some things can be done with either technique, but some things need one or the other! Expect to need both."

.. Change to a standard page
.. raw:: pdf

    PageBreak standardPage

Voice API Examples
==================

*  IVR

  -  Incoming call, serve NCCO to answer it
  -  Prompt user for DTMF input
  -  DTMF input arrives as a webhook, return a new NCCO

*  Proxy

  -  Incoming call, serve NCCO to answer it
  -  Put user into conference
  -  API call to place outgoing call to other user, with NCCO to join same conference

.. raw:: pdf

  TextAnnotation "IVR = Interactive Voice Response"

  TextAnnotation "Use the proxy to allow customers to connect with staff (for example) without revealing actual numbers"

  TextAnnotation "Next: more detail on webhooks"

Voice Webhooks
==============

* Webhooks are events over HTTP

* Nexmo sends information about events and changes in call state as they happen

* These events are webhooks: incoming HTTP requests
  
* Your application needs to be able to receive requests and respond

|

The URL is set up in advance, as part of the application configuration

.. raw:: pdf

  TextAnnotation "Think of it as a load of pings and beeps to let you know things are happening :)"

  TextAnnotation "As well as making API calls, handling webhooks needs your application to receive incoming requests. We'll talk about how to do that on dev platforms in two slides' time"

  TextAnnotation "Must ack the webhook, in a specific timeframe. Nexmo will retry if not"

  TextAnnotation "Set your URLs through the dashboard or via CLI when you create your application configuration and register a phone number to it"


Voice Webhooks
==============

Webhooks can be expected:

-  When the call is answered, an HTTP request to the ``answer_url``
-  When events such as "ringing", "answered", "completed" occur, HTTP requests to the ``event_url``
-  Keypad digits from an ``input`` action are sent to the specified URL
-  When a recording is completed, an HTTP request to the ``recording_url``
-  When a ``notify`` action in an NCCO is processed

.. raw:: pdf

  TextAnnotation "Answer webhook when someone calls your Nexmo number. Nexmo servers hit your URL and you return an NCCO"

  TextAnnotation "Events show up at the ``event_url``. This is great for knowing what is going on - errors go there too!"

  TextAnnotation "DTMF input results in a webhook with a ``dtmf`` field, you return an NCCO"

  TextAnnotation "When recording is ready, webhook to ``recording_url`` has a link to the file to download"

  TextAnnotation "``notify`` is an NCCO action that sends a webhook to a URL. The NCCO continues afterwards, useful for progress indicators"

  TextAnnotation "There are some tricks to working with webhooks locally: I'd like to share some tips"

Webhooks on Dev Platforms
=========================

https://ngrok.com/ - secure tunnel to your dev platform

|

Use this tool to:

- webhook into code running locally
- inspect the request and response of the webhook
- replay requests and see the responses

.. raw:: pdf

  TextAnnotation "Proprietary tool with a free tier"

  TextAnnotation "Get a paid account to get a static URL so you don't have to update your webhook configs so often!"

  TextAnnotation "You could also push to cloud"

Ngrok for Testing Webhooks
==========================

Start the tunnel on your laptop: receive a public URL

|

.. image:: images/Ngrok.png
    :width: 12cm

|

We have a blog post about this: https://www.nexmo.com/blog/2017/07/04/local-development-nexmo-ngrok-tunnel-dr

.. raw:: pdf
  TextAnnotation "Google Nexmo and Ngrok to find the post, or see the resources section in the GitHub Repo"

  TextAnnotation "This makes quite a neat demo for anyone who hasn't seen it before. Start a local webserver with basic test script, make some curl requests to it, then show the console interface and web dashboard and replay button."

  TextAnnotation "Encourage people to download/install while I'm talking ..."

The Answer Webhook
==================

When someone calls your Nexmo number, you get a webhook like this:

.. code:: json

  {
    "from": "442079460000",
    "to": "447700900000",
    "uuid": "aaaaaaaa-bbbb-cccc-dddd-0123456789ab",
    "conversation_uuid": "CON-aaaaaaaa-bbbb-cccc-dddd-0123456789ab"
  }

|

Your code must return a valid NCCO

.. raw:: pdf

  TextAnnotation "Compare with when we do an outgoing call, we can either specify an ``answer_url`` and serve an NCCO, or provide the NCCO when making the call"

The Event Webhook
=================

Many different events can produce webhooks to the ``event_url``:

* Changes in call state e.g. "ringing"/"answered"
* ``record`` and ``input`` actions can specify a URL, which may be the same as the event URL
* Errors will also be sent to the ``event_url``

|

Detailed reference: https://developer.nexmo.com/voice/voice-api/webhook-reference#event-webhook

Voice Events Logger
===================

A tool you can use to direct your ``event_url`` to, it just acknowledges the webhook and displays what arrived.

|

https://github.com/Nexmo/voice-event-logger - it can be run locally or deployed to Heroku

.. raw:: pdf

  TextAnnotation "A very basic debugging tool to get you started. In a 'real' application you would want to handle the events yourself."

Pieces of the Voice API
=======================

.. image:: images/api-diag.JPG
  :width: 14cm

Further Reading
===============

* Exercises at https://voice-workshop.nexmodev.com/
* Our blog https://nexmo.com/blog
* Tell us what you think! ``@NexmoDev`` on twitter


