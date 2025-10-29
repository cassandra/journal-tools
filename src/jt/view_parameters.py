from dataclasses import dataclass

from django.http import HttpRequest


@dataclass
class ViewParameters:
    """ For session state """
    
    journal_id         : int  = None

    def to_session( self, request : HttpRequest ):
        if not hasattr( request, 'session' ):
            return
        request.session['journal_id'] = str(self.journal_id)
        return

    @staticmethod
    def from_session( request : HttpRequest ):
        if not request:
            return ViewParameters()
        if not hasattr( request, 'session' ):
            return ViewParameters()
        try:
            journal_id = int( request.session.get( 'journal_id' ))
        except ( TypeError, ValueError ):
            journal_id = None

        return ViewParameters(
            journal_id = journal_id,
        )
    
