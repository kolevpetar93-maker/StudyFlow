import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:studyflow/main.dart';

void main() {
  testWidgets('Prazna aplikacija se zazene brez napak', (tester) async {
    await tester.pumpWidget(const StudyFlowApp());

    expect(find.byType(Scaffold), findsOneWidget);
    expect(tester.takeException(), isNull);
  });
}
