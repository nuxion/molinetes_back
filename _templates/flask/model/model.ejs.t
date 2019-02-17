---
to: <%= h.package %>/models/<%= name %>.py
---
from . import db

class <%=Name%=>(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __repr__(self):
        return '<<%= Name %> %r' % self.name
