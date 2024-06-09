from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Example legal document text
document_text = """
                This License Agreement ("Agreement") is made and entered into by and between Company X, a corporation organized and existing under the laws of the State of California, with its principal place of business at 123 Main Street, Cityville, California, and User Y, an individual residing at 456 Oak Avenue, Townville, California.

WHEREAS, Company X owns and operates a software application known as "Product Z," which provides online collaboration and project management services; and

WHEREAS, User Y desires to obtain a license to use the Product Z software for personal and non-commercial purposes;

NOW, THEREFORE, in consideration of the mutual covenants and agreements contained herein, the parties agree as follows:

1. License Grant. Subject to the terms and conditions of this Agreement, Company X hereby grants User Y a non-exclusive, non-transferable license to use the Product Z software for personal and non-commercial purposes during the term of this Agreement.

2. Restrictions. User Y shall not (a) modify, adapt, or create derivative works based on the Product Z software; (b) sublicense, lease, rent, or otherwise transfer the Product Z software to any third party; (c) reverse engineer, decompile, or disassemble the Product Z software; or (d) use the Product Z software in any manner that violates applicable laws or regulations.

3. Term and Termination. This Agreement shall commence on the effective date and continue in full force and effect until terminated by either party. Either party may terminate this Agreement at any time upon written notice to the other party.

4. Confidentiality. User Y acknowledges that the Product Z software contains confidential information and trade secrets of Company X. User Y agrees to maintain the confidentiality of the Product Z software and not disclose it to any third party.

5. Limitation of Liability. In no event shall Company X be liable for any indirect, incidental, special, or consequential damages arising out of or in connection with this Agreement, even if Company X has been advised of the possibility of such damages.

6. Governing Law. This Agreement shall be governed by and construed in accordance with the laws of the State of California, without regard to its conflict of law principles.

7. Entire Agreement. This Agreement constitutes the entire agreement between the parties with respect to the subject matter hereof and supersedes all prior and contemporaneous agreements and understandings, whether written or oral, relating to such subject matter.

IN WITNESS WHEREOF, the parties have executed this Agreement as of the date first above written.

                """

# Parse the document text
parser = PlaintextParser.from_string(document_text, Tokenizer("english"))

# Initialize the LSA summarizer
lsa_summarizer = LsaSummarizer()

# Get the summary with 1 sentence (for brevity)
summary = lsa_summarizer(parser.document, 1)

# Print the summary
for sentence in summary:
    print(sentence)
