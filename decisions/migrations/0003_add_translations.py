# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 08:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('decisions', '0002_organization_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(help_text='Title of the action', max_length=255)),
                ('resolution', models.CharField(blank=True, help_text='Resolution taken in this action (like tabled, decided...)', max_length=255)),
            ],
            options={
                'db_table': 'decisions_action_translation',
                'default_permissions': (),
                'managed': True,
                'db_tablespace': '',
                'verbose_name': 'action Translation',
            },
        ),
        migrations.CreateModel(
            name='AttachmentTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(blank=True, help_text='Short name of this attachment', max_length=400)),
                ('confidentiality_reason', models.CharField(blank=True, help_text='Reason for keeping this attachment confidential', max_length=100)),
            ],
            options={
                'db_table': 'decisions_attachment_translation',
                'default_permissions': (),
                'managed': True,
                'db_tablespace': '',
                'verbose_name': 'attachment Translation',
            },
        ),
        migrations.CreateModel(
            name='CaseGeometryTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
            options={
                'db_table': 'decisions_casegeometry_translation',
                'default_permissions': (),
                'managed': True,
                'db_tablespace': '',
                'verbose_name': 'case geometry Translation',
            },
        ),
        migrations.CreateModel(
            name='CaseTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(help_text='Descriptive compact title for this case', max_length=255)),
            ],
            options={
                'db_table': 'decisions_case_translation',
                'default_permissions': (),
                'managed': True,
                'db_tablespace': '',
                'verbose_name': 'case Translation',
            },
        ),
        migrations.CreateModel(
            name='ContentTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(blank=True, help_text='Title of this content', max_length=255)),
                ('type', models.CharField(help_text='Type of this content (options include: decision, proposal, proceedings...)', max_length=255)),
                ('hypertext', models.TextField(help_text='Content formatted with pseudo-HTML. Only a very restricted set of tags is allowed. These are: first and second level headings (P+H1+H2) and table (more may be added, but start from a minimal set)')),
            ],
            options={
                'db_table': 'decisions_content_translation',
                'default_permissions': (),
                'managed': True,
                'db_tablespace': '',
                'verbose_name': 'content Translation',
            },
        ),
        migrations.CreateModel(
            name='EventTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(blank=True, help_text="The event's name", max_length=255)),
            ],
            options={
                'db_table': 'decisions_event_translation',
                'default_permissions': (),
                'managed': True,
                'db_tablespace': '',
                'verbose_name': 'event Translation',
            },
        ),
        migrations.CreateModel(
            name='FunctionTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(help_text='Name of this function', max_length=255)),
            ],
            options={
                'db_table': 'decisions_function_translation',
                'default_permissions': (),
                'managed': True,
                'db_tablespace': '',
                'verbose_name': 'function Translation',
            },
        ),
        migrations.CreateModel(
            name='OrganizationClassTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'decisions_organizationclass_translation',
                'default_permissions': (),
                'managed': True,
                'db_tablespace': '',
                'verbose_name': 'organization class Translation',
            },
        ),
        migrations.CreateModel(
            name='OrganizationTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(help_text='A primary name, e.g. a legally recognized name', max_length=255)),
            ],
            options={
                'db_table': 'decisions_organization_translation',
                'default_permissions': (),
                'managed': True,
                'db_tablespace': '',
                'verbose_name': 'organization Translation',
            },
        ),
        migrations.CreateModel(
            name='PostTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('label', models.CharField(help_text='A label describing the post', max_length=255)),
            ],
            options={
                'db_table': 'decisions_post_translation',
                'default_permissions': (),
                'managed': True,
                'db_tablespace': '',
                'verbose_name': 'post Translation',
            },
        ),
        migrations.RemoveField(
            model_name='action',
            name='resolution',
        ),
        migrations.RemoveField(
            model_name='action',
            name='title',
        ),
        migrations.RemoveField(
            model_name='attachment',
            name='confidentiality_reason',
        ),
        migrations.RemoveField(
            model_name='attachment',
            name='name',
        ),
        migrations.RemoveField(
            model_name='case',
            name='title',
        ),
        migrations.RemoveField(
            model_name='content',
            name='hypertext',
        ),
        migrations.RemoveField(
            model_name='content',
            name='title',
        ),
        migrations.RemoveField(
            model_name='content',
            name='type',
        ),
        migrations.RemoveField(
            model_name='event',
            name='name',
        ),
        migrations.RemoveField(
            model_name='function',
            name='name',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='name',
        ),
        migrations.RemoveField(
            model_name='organizationclass',
            name='name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='label',
        ),
        migrations.RemoveField(
            model_name='casegeometry',
            name='name',
        ),
        migrations.AlterUniqueTogether(
            name='casegeometry',
            unique_together=set([('data_source', 'origin_id')]),
        ),
        migrations.AddField(
            model_name='posttranslation',
            name='master',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='decisions.Post'),
        ),
        migrations.AddField(
            model_name='organizationtranslation',
            name='master',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='decisions.Organization'),
        ),
        migrations.AddField(
            model_name='organizationclasstranslation',
            name='master',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='decisions.OrganizationClass'),
        ),
        migrations.AddField(
            model_name='functiontranslation',
            name='master',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='decisions.Function'),
        ),
        migrations.AddField(
            model_name='eventtranslation',
            name='master',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='decisions.Event'),
        ),
        migrations.AddField(
            model_name='contenttranslation',
            name='master',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='decisions.Content'),
        ),
        migrations.AddField(
            model_name='casetranslation',
            name='master',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='decisions.Case'),
        ),
        migrations.AddField(
            model_name='casegeometrytranslation',
            name='master',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='decisions.CaseGeometry'),
        ),
        migrations.AddField(
            model_name='attachmenttranslation',
            name='master',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='decisions.Attachment'),
        ),
        migrations.AddField(
            model_name='actiontranslation',
            name='master',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='decisions.Action'),
        ),
        migrations.AlterUniqueTogether(
            name='posttranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='organizationtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='organizationclasstranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='functiontranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='eventtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='contenttranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='casetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='casegeometrytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='attachmenttranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='actiontranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
