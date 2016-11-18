# Yeah, nah as a Service (YNaaS)

## About

Needed a way to give a Yeah, Nah response in a suitably dramatic, troll-worthy way.

It's built on Flask and uses the MIT license (so feel free to extend as you wish).

## Usage

Running:

```
$ export FLASK_APP=hello.py
$ flask run
 * Running on http://127.0.0.1:5000/

```

Calling:

```
GET http://<server>:<port>/
```
Results in:

`Yeah, nah.`

```
GET http://<server>:<port>/<thing>
```
Results in:

`<thing> ? Yeah, nah.`

So you might do

```
GET http://127.0.0.1/sandwich for lunch?/
```

And the service will say:

`sandwich for lunch? Yeah, nah.`