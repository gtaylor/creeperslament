# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'BlogPost.date_last_modified'
        db.add_column('blog_blogpost', 'date_last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2011, 3, 20, 18, 49, 45, 910972), blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'BlogPost.date_last_modified'
        db.delete_column('blog_blogpost', 'date_last_modified')


    models = {
        'blog.blogcategory': {
            'Meta': {'ordering': "['name']", 'object_name': 'BlogCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'})
        },
        'blog.blogpost': {
            'Meta': {'ordering': "['-date_added']", 'object_name': 'BlogPost'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blog.BlogCategory']", 'symmetrical': 'False'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['blog']
