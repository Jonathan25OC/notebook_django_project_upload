from django.shortcuts import render
import pandas as pd

def index(request):
    resultados = None
    if request.method == "POST" and request.FILES.get("csv_file"):
        csv_file = request.FILES["csv_file"]
        df = pd.read_csv(csv_file)

        # Aquí pones la lógica del notebook
        resultados = df.describe().to_html(classes="table table-striped")

    return render(request, "analysis_app/index.html", {"resultados": resultados})


