# tskit-dev/administrative <img align="right" width="145" height="90" src="tskit_logo.ink.svg">
This repository contains project management documents and discussions for
development of the tree sequence toolkit (tskit). Tree sequences are a flexible and
compact way of representing genetic history and storing DNA variation data.

## Contributing

We encourage contributions to improve any of the
[tskit development repositories](https://github.com/tskit-dev).
Improvements to documentation are particularly welcome, and are likely to be accepted
quickly. 

The preferred way to contribute is to create your own fork of the appropriate
repository (for instance, `tskit-dev/tskit`), make changes, and submit your changes as a
pull request (PR). A simple way to do this is to create a topic branch based on upstream,
via the following git commands from within your forked repository:

```
$ git fetch upstream
$ git checkout upstream/master
$ git checkout -b my-topic-branch
# Do work and add commits.
$ git push origin my-topic-branch
# Go to github & open a PR based on my-topic-branch (the option appears automatically).
```

Python contributions should conform to [PEP-8](https://www.python.org/dev/peps/pep-0008/)
with lines limited to a maximum of 89 characters, and no trailing whitespace.
We prefer contributions to documentation to follow this style where possible.

All submissions are accepted on the basis that they have been provided to the tskit
project under the [MIT License](https://opensource.org/licenses/MIT).