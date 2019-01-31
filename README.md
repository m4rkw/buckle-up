# buckle-up by m4rkw

A python toolbox for writing macOS sandbox profiles.

## installation

````
pip3 install buckle-up
````

## monitor all sandbox events

````
bu -p all
````

## monitor sandbox events for specific processes

````
bu -p 'Slack,Slack Helper'
````

## write denied actions to a sandbox profile file

````
bu -p 'Slack,Slack Helper' -o slack.sb
````

## known issues

deny events are de-duped but mostly written verbatim from the system log into
the output sandbox profile. this means that most references are entered as
"literal" and some actions such as signals will not be in a valid format so
some manual tidying will be necessary. there is the beginnings of support for
different target nouns but this is far from complete.
