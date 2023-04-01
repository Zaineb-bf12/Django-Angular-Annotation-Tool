
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from .models import Document, Annotation

class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotation
        fields = ['id', 'start', 'end', 'label', 'annotated_text']

@api_view(['POST'])
def create_annotation(request):
    document_id = request.data.get('document_id')
    start = request.data.get('start')
    end = request.data.get('end')
    label = request.data.get('label')
    annotated_text = request.data.get('annotated_text')

    document = Document.objects.get(id=document_id)
    annotation = Annotation.objects.create(
        document=document,
        start=start,
        end=end,
        label=label,
        annotated_text=annotated_text
    )
    return Response(AnnotationSerializer(annotation).data)

@api_view(['GET'])
def export_annotations(request, document_id):
    document = Document.objects.get(id=document_id)
    annotations = Annotation.objects.filter(document=document)
    data = {
        'document_text': document.text,
        'annotations': AnnotationSerializer(annotations, many=True).data
    }
    return Response(data)

@api_view(['GET'])
def list_labels(request):
    labels = Annotation.objects.values_list('label', flat=True).distinct()
    return Response(labels)
