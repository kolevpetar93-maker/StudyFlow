import 'package:flutter_test/flutter_test.dart';
import 'package:studyflow/main.dart';

void main() {
  testWidgets('Začetna aplikacija se zažene brez napak', (tester) async {
    await tester.pumpWidget(const StudyFlowApp());

    expect(find.text('StudyFlow'), findsOneWidget);
    expect(tester.takeException(), isNull);
  });
}
