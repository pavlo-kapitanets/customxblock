import pkg_resources
from web_fragments.fragment import Fragment
from xblock.core import XBlock



class SimpleXBlock(XBlock):
    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        html = self.resource_string("static/html/simplexblock.html")
        frag = Fragment(html.format(self=self))
        frag.add_css(self.resource_string("static/css/simplexblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/simplexblock.js"))
        frag.initialize_js('SimpleXBlock')
        return frag

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("SimpleXBlock",
             """<simplexblock/>
             """),
            ("Multiple SimpleXBlock",
             """<vertical_demo>
                <simplexblock/>
                <simplexblock/>
                <simplexblock/>
                </vertical_demo>
             """),
        ]
