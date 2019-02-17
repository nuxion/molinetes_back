---
inject: true
to: <%= h.package %>/models/__init__.py
after: shortcuts
---
from .<%= name%> import <%= Name %>
