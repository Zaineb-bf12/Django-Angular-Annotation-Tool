
import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-annotation',
  templateUrl: './annotation.component.html',
  styleUrls: ['./annotation.component.css']
})
export class AnnotationComponent {
  labels ='';
  selectedLabel = '';
  labelsList = '';

  constructor(private http: HttpClient) {}

  submitLabels() {
    const data = { labels: this.labels.split(',') };
    this.http.post('/api/labels/', data).subscribe();
  }}