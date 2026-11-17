import 'package:flutter/material.dart';

void main() {
  runApp(const StudyFlowApp());
}

// Začetna osnova. Posamezne zaslone in navigacijo dodamo pozneje.
class StudyFlowApp extends StatelessWidget {
  const StudyFlowApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'StudyFlow',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(seedColor: const Color(0xFF8062D6)),
        scaffoldBackgroundColor: const Color(0xFFFAF9FD),
      ),
      home: Scaffold(
        appBar: AppBar(title: const Text('StudyFlow')),
        body: const SafeArea(
          child: Center(
            child: SingleChildScrollView(
              padding: EdgeInsets.all(24),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Icon(
                    Icons.auto_stories_rounded,
                    size: 64,
                    color: Color(0xFF8062D6),
                  ),
                  SizedBox(height: 24),
                  Text(
                    'Učenje v tvojem ritmu.',
                    textAlign: TextAlign.center,
                    style: TextStyle(fontSize: 28, fontWeight: FontWeight.w600),
                  ),
                  SizedBox(height: 12),
                  Text(
                    'Inteligentni načrtovalnik učenja',
                    textAlign: TextAlign.center,
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
