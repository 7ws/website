from django.views import generic


class Home(generic.TemplateView):

    """A simple landing page
    """

    template_name = 'home.html'
