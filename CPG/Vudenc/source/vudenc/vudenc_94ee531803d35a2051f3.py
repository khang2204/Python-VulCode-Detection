def test_send_email(self):...
"""docstring"""
send_email(context_data={'milestone': 'first', 'students_number': 2,
    'course_title': 'Test Course', 'lesson_title': 'Test Lesson',
    'current_site': Site.objects.get_current(), 'course_id': 1,
    'unit_lesson_id': 1, 'courselet_pk': 1}, from_email=settings.EMAIL_FROM,
    to_email=['test@example.com'], template_subject=
    'ct/email/milestone_ortc_notify_subject', template_text=
    'ct/email/milestone_ortc_notify_text')
self.assertEqual(len(mail.outbox), 1)
