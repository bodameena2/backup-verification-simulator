from app.pdf_generator import generate_pdf


def test_generate_pdf_returns_pdf_bytes():
<<<<<<< HEAD
    title = "Test Report"
    content = "Status: PASS\n\nDetails:\n[+] All checks passed\n"
    pdf_bytes = generate_pdf(title, content)
    assert isinstance(pdf_bytes, (bytes, bytearray))
    assert len(pdf_bytes) > 0
    # PDF files start with %PDF
    assert pdf_bytes[:4] == b"%PDF"
=======
    pdf_bytes = generate_pdf(
        "Verification Report: backup.db",
        "Status: PASS\n\nDetails:\n[+] Users table count: 100\n\nAI Narrative Report:\nBackup is healthy.",
    )

    assert isinstance(pdf_bytes, bytes)
    assert pdf_bytes.startswith(b"%PDF")
    assert len(pdf_bytes) > 1000
>>>>>>> 8f8e9ae6d3a64d69cdcb2697c043aba3aa99a759
