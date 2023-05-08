# Ad Server

The **Ad Server** is a server that provides an advertisement to display, if any are available, in the form of a [UI XML](UI_XML "wikilink") and PNG image. These were only usually used to promote new games by Mediocre, but if reworked, they could be used to advertise new versions of mods, among other things.

## Breakdown

### Retrieving adverts

The advertisements are retrieved in `HttpThread::checkBanners` in `libsmashhit.so`.

The initial request is an HTTP/1.1 GET request for:

`http://mediocre.se/content/smashhit/ads.php?platform={platform}&version={version}&rev={rev}&date={date}`

* `platform`: The platform that the user is on; for example, `android`.
* `version`: The string of the version of the game that the user is on; for example, `1.4.2`.
* `rev`: Unknown, but probably the current advertisement revision.
* `date`: The date, unknown format.

The server responds with a zero-length document if there is no ad. If
there is an advert to display, however, it will respond with an XML
document. The format of the XML document is:

``` xml
<ads revision="{revision}" showfront="{showfront}" onlyfree="{onlyfree}" sale="{sale}" folder="{folder}"/>
```

* `revision`: The revision of the new advertisements. If zero, there are none and no other fields need to be filled.
* `showfront`: Unknown, but seems to prevent downloading new advert if equal to zero.
* `onlyfree`: Unknown, but probably if the ad should only be shown to free (non-premium) users.
* `sale`: Unknown, but seems to be if this is a sale on premium or not.
* `folder`: The subfolder where the ads.xml and ads.png are stored.

Note that the folder is of the `https://mediocre.se/content/smashhit/` part of the URL, or whatever you have for your adserver.

Assuming that `revision` and `showfront` are non-zero values, the game will download the `ads.png` and `ads.xml` files from the folder and complete successfully if they both exist.

### Display

The advertisements seem to be in the normal UI XML format with a PNG
file for display, so they are just shown like any other UI element.

## Examples

### Official ad server

Try visiting this URL:

```url
https://mediocre.se/content/smashhit/ads.php?platform=android&version=1.4.3&rev=3&date=1470157898
```

Right click and inspect the page source.

You should see that the server has responded with `<ads revision="0"/>`, assuming there are not any ads right now.

**Note**: Your browser might add some extra HTML because it assumes this is an HTML document, but it is not.

### Crafted response

An example of a response might be:

``` xml
<ads revision="1" showfront="1" onlyfree="0" sale="0" folder="dirac"/>
```

For the following files:

* `https://mediocre.se/content/smashhit/dirac/ads.png`
* `https://mediocre.se/content/smashhit/dirac/ads.xml`

## See also

* [Smash Hit Ad Server reimplementation](https://github.com/knot126/Smash-Hit-Ad-Server) by Knot126
