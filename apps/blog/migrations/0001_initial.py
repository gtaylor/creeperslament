# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'BlogCategory'
        db.create_table('blog_blogcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('blog', ['BlogCategory'])

        # Adding model 'BlogPost'
        db.create_table('blog_blogpost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('blog', ['BlogPost'])

        # Adding M2M table for field category on 'BlogPost'
        db.create_table('blog_blogpost_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('blogpost', models.ForeignKey(orm['blog.blogpost'], null=False)),
            ('blogcategory', models.ForeignKey(orm['blog.blogcategory'], null=False))
        ))
        db.create_unique('blog_blogpost_category', ['blogpost_id', 'blogcategory_id'])


    def backwards(self, orm):
        
        # Deleting model 'BlogCategory'
        db.delete_table('blog_blogcategory')

        # Deleting model 'BlogPost'
        db.delete_table('blog_blogpost')

        # Removing M2M table for field category on 'BlogPost'
        db.delete_table('blog_blogpost_category')


    models = {
        'blog.blogcategory': {
            'Meta': {'ordering': "['name']", 'object_name': 'BlogCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'blog.blogpost': {
            'Meta': {'ordering': "['-date_added']", 'object_name': 'BlogPost'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blog.BlogCategory']", 'symmetrical': 'False'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['blog']
