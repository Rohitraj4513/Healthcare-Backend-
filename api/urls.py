from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import RegisterView, PatientListCreateView, PatientDetailView, DoctorListCreateView, DoctorDetailView, MappingListCreateView, MappingDetailView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('patients/', PatientListCreateView.as_view(), name='patient_list_create'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('doctors/', DoctorListCreateView.as_view(), name='doctor_list_create'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('mappings/', MappingListCreateView.as_view(), name='mapping_list_create'),
    path('mappings/<int:pk>/', MappingDetailView.as_view(), name='mapping_detail'),
]
