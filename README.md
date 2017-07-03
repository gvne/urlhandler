# URL Handler

A step by step example of how to create a URL handler in python on Mac OS.

URL handler are most useful in protocols that send response through a redirect
URI such as `OAuth2`.

## Quick Start

##### Make an application
Open the `src/urlhandler.scpt` script with the Script Editor application and
export it as an Application in a local folder.

##### Package the script
Run the package script:
```bash
python conf/package_app.py /path/to/exported/app.py
```
Copy the exported application to the Application folder

##### Set the script to be executed on url call
```bash
defaults write com.gvne.urlhandler Script /path/to/this/folder/src/script.py
```

##### Test it !
In Safari type the url `gvne://something`. Your script got executed with the url
as first arg !  
You can check the output by doing `cat /tmp/write_args_script.log`

## Development steps

### Handle custom URI

Mac OS natively allows creating an URL handler for Applications. To use that
tool we need to make an Application. The easiest way is to use an AppleScript.  
Such a script is available in src/urlhandler.scpt. Its content will be discussed
later.  
To create an application out of this script, open it with the Script Editor app
and export it as an application.

To make this application answer to our custom URI, we need to edit its
`Info.plist`. A script got created to do so for you:
```bash
python conf/patch_app.py path/to/exported/urlhandler.app
```
It makes the application answer to url with the `gvne://` scheme.
To test it you can copy the app to your Application folder and open an url such
as `gvne://mytestfunction?param1=value1&param2=value2` from safari. If correctly
setup, safari should ask you if you want to let the "urlhandler" application
answer. Click Authorize and the script will be executed.

### From AppleScript to Python

When you look at the script `src/urlhandler.scpt`, you realize it calls a python
script called `urlhandler.py` and located in the bundle.  
That script can be found in the src folder. All it does is read the
`com.gvne.urlhandler` preferences and execute the script value with the url as
first arg.
To package the application correctly, a script exist:
```bash
python conf/package_app.py path/to/exported/urlhandler.app
```
NB: this script installs the script and the url handler. The `patch_app.py`
script shouldn't be executed before this one.  

To tie your local python script, you need to update the preferences:
```bash
defaults write com.gvne.urlhandler Script path/to/my/script.py
```

Once setup, you can copy the app in you Application folder and test it with
safari. Your script should be executed.

## Sources

[URL handler basis](https://stackoverflow.com/questions/2418910/osx-defining-a-new-url-handler-that-points-straight-at-a-python-script  )
