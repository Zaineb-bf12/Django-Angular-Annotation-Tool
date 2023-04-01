import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms'; 
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AnnotationComponent } from "./annotation/annotation.component";
import { DocumentViewComponent } from './document-view/document-view.component';

@NgModule({
  declarations: [
    AppComponent,
    AnnotationComponent,
    DocumentViewComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
