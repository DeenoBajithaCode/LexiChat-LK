# lexichat/views.py

import os
from django.shortcuts import render
from .forms import QuestionForm
from utils.qa_chain import build_qa_chain

PDF_PATH = os.path.join('data', 'constitution.pdf')

# Build the QA chain once at startup
qa_chain = build_qa_chain(PDF_PATH)

def index(request):
    answer = None

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            result = qa_chain(question)
            answer = result['result']
    else:
        form = QuestionForm()

    return render(request, 'lexichat/index.html', {'form': form, 'answer': answer})
