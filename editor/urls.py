from django.urls import path

from editor.views import *

app_name="editor"
urlpatterns = [ 

    path('post/', RichEditorView.as_view(), name="richeditor"),
    path('gen-rich-editor/', RichEditorGen.as_view(), name="richeditor_gen"),
]
