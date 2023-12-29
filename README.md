# BlockReplace (BloRP)

Replaces placeholders in documents (navbar, ...) with HTML "components", for cases where really simple, yet efficient websites are desired (e.g., personal homepage)

## Goals and Scope
This tool allows you to build a simple website that has *navbar and footer or similar re-occurring components* defined *exactly once*, *without* using any

* JS frameworks that perform client-side composition of your page,
* complex PHP bakers that would do the same server-side or
* other complex build steps with potentially bloated dependency trees etc.

In contrast, this is just a simple python script without any dependencies, which replaces stuff in your HTML so you can build a simple, static homepage with pure HTML and CSS, and that's really all it is or does.

## Sample Use
```
python .\blorp.py -i input-sample -o output-sample
```

## Limitations
* In contrast to ShadowDOM or related ideas, this script really has the sole objective of making it possible to have the re-occuring bits of a website (usually: navbar and footer) being defined only once. At the end, everything will just be part of the same website, and share the same namespace in CSS, etc. (which might not be a problem for many simple projects, but potentially for bigger apps, and this little script here really doesn't claim to solve that all).
* Indentation is read from the input block file and kept as-is, block definitions should not have any indentation in the input HTML file.
* Block definitions must currently be 100% matching the schema - including (absence of) whitespace and lower/upper case, etc.
* Currently, the input directory and output directory will be considered flat (subdirectory structures will not be parsed or replicated).


WARNING: If you're a modern web developer, this project might hurt your personal honor or feelings. Investigate and use at your own risk! ;-)

## LICENSE
This tool is available under the MIT license.
