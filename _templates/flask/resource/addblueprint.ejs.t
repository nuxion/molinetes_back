---
inject: true
to: <%= h.package %>/__init__.py
after: add_routes
---
from . import <%= name %>
app.register_blueprint(<%= name %>.bp, url_prefix='{}'.format(prefix))
