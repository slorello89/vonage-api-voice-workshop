Receiving Webhooks with Ngrok
=============================

> Major disclaimer about public ngrok and user-supplied content. If anything happens that could hurt the demo, or I see any content that could impact anyone in the room, the demo stops and you just get talking.

**Write some code to accept incoming webhook, and test it**

Create code in ``hook.php``:

.. code:: php

    <?php

    error_log(print_r($_REQUEST, true));
    echo "OK";

Start webserver ``php -S localhost:8080``

Try a webhook (use a browser) making a GET request to ``http://localhost:8080/hook.php``, add some params ``?dinner=pizza``

**Ngrok**

Explain what Ngrok does and when to use it (local dev, APIs or websites)

Start an ngrok tunnel ``ngrok http 8080``.

Try the webhook again at this URL, with (different) params

And show the ngrok dashboard http://localhost:4040

