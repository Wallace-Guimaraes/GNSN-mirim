from django.urls import path
from mirim import views

app_name = "mirim"

urlpatterns = [
    path("home/", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("frequencia/", views.frequencia, name="frequencia"),
    path("guardas/", views.listaGuarda, name="guardas"),
    path("cadastro-evento/", views.cadastroEvento, name="cadastro_evento"),
    path("eventos/", views.eventos, name="eventos"),
    path("relatorio/", views.relatorio, name="relatorio"),
    path("admin/", views.admin, name="admin"),
]