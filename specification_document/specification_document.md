qcML :

Status of This Document

This document presents a final specification for the qcML data format developed by the HUPO Proteomics Standards Initiative. Distribution is unlimited.

Version of This Document

The current version of this document is: version X.X

# 		

# Abstract

**Contents**

[[TOC]]

1. Introduction

    1. Background

    2. Document Structure

The remainder of this document is structured as follows. Section 2 lists use cases qcML is designed to.

2. Use Cases for qcML

3. Concepts and Terminology

4. Relationship to Other Specifications

    3. Important concepts from FuGE

    4. The PSI Mass Spectrometry Controlled Vocabulary (CV)

    5. Validation of controlled vocabulary terms

        1. Validation of values used within CvParams

    6. Change from version X.X.X

5. Resolved Design and scope issues

        2. Handling updates to the controlled vocabulary

. 

        3. Use of qcML for analysis pipelines

    7. Encoding zeroes, nulls, infinity and calculation errors

    8. Protein grouping

    9. Comments on Specific Use Cases

        4. MS1 label-free intensity

        5. MS1 label-based

        6. MS2 spectral counting

        7. MS2 tag-based 

        8. Selected Reaction Monitoring (SRM)

    10. Semantic validation rules

    11. Other supporting materials

    12. Open Issues

6. Model in XML Schema

**Figure 1 A diagrammatic overview of the ****qcML**** schema.**

    13. Element <qcML>

<table>
  <tr>
    <td>Graphical Context:</td>
    <td></td>
  </tr>
  <tr>
    <td>Example Context:</td>
    <td></td>
  </tr>
</table>


7. Specific Comments on schema 

In this section, several points of documentation are elaborated beyond the core specification in Section 6.

    14. File extension and compression

It is noted that standard file compression algorithms greatly reduce the qcML file sizes, speeding up file transfers and uploads / downloads. It is also noted that software implementing qcML import or export will be expected to benefit in performance from working with compressed qcML, since the compression and decompression algorithms are expected to give significant performance gains over disk access times for non-compressed files. As such, it is RECOMMENDED that qcML files are compressed using gzip from all software that exports qcML and software that imports SHOULD be expected to read gzipped files, as well as native (non-compressed) qcML files. The file extension for native qcML files SHOULD be ".mzq" and for compressed files SHOULD be “mzq.gz”.

    15. Referencing elements within the document

A number of elements within the schema have an attribute which is used to reference an element elsewhere in the file using the unique identifier of the referenced element. These attributes are named following the convention: "[elementName]_ref". The uniqueness of the value in the “id” attribute of elements is validated using xsd:ID, and the integrity of the reference is validated using xsd:IDREF, defined within the schema. As such, using XML Schema validation alone, it would be possible to reference an incorrect type of element (since IDREF does not enforce the type of element). However, for a file to be semantically valid, references to the correct type of element MUST be provided and the semantic validation software checks these rules.

    16. Unknown modifications

In version 1.0.0, only cvParam elements can be given on <PeptideConsensus>:<Modification> and a term "unknown modification" has been added to the PSI-MS CV. This term MUST only be used if the identified modification is not present in UNIMOD (or other allowed CV), according to the identity of the residue modified and the delta mass, within the parent tolerance specified in the search. The semantic validator will check any uses of the “unknown modification” term (MS:1001460) and reject files if the modification is present in UNIMOD. 

8. Conclusions

This document contains the specifications for using the qcML format to represent results from peptide and protein identification pipelines, in the context of a proteomics investigation. This specification, in conjunction with the XML Schema, mapping file and CV constitute a proposal for a standard from the Proteomics Standards Initiative. These artefacts are currently undergoing the PSI document process standardization process, which will result in a standard officially sanctioned by PSI.

9. Authors and Contributors

Authors of this specification:

* Mathias Walzer, Center for Bioinformatics/Dept. of Computer Science, University of Tübingen, Sand 14, 

.

10. References

* [http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4125725/](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4125725/)

11. Intellectual Property Statement

The PSI takes no position regarding the validity or scope of any intellectual property or other rights that might be claimed to pertain to the implementation or use of the technology described in this document or the extent to which any license under such rights might or might not be available; neither does it represent that it has made any effort to identify any such rights. Copies of claims of rights made available for publication and any assurances of licenses to be made available, or the result of an attempt made to obtain a general license or permission for the use of such proprietary rights by implementers or users of this specification can be obtained from the PSI Chair.

The PSI invites any interested party to bring to its attention any copyrights, patents or patent applications, or other proprietary rights that may cover technology that may be required to practice this recommendation. Please address the information to the PSI Chair (see contacts information at PSI website).

# Copyright Notice

Copyright (C) Proteomics Standards Initiative (2013). All Rights Reserved.

This document and translations of it may be copied and furnished to others, and derivative works that comment on or otherwise explain it or assist in its implementation may be prepared, copied, published and distributed, in whole or in part, without restriction of any kind, provided that the above copyright notice and this paragraph are included on all such copies and derivative works. However, this document itself may not be modified in any way, such as by removing the copyright notice or references to the PSI or other organizations, except as needed for the purpose of developing Proteomics Recommendations in which case the procedures for copyrights defined in the PSI Document process must be followed, or as required to translate it into languages other than English.

The limited permissions granted above are perpetual and will not be revoked by the PSI or its successors or assigns.

This document and the information contained herein is provided on an "AS IS" basis and THE PROTEOMICS STANDARDS INITIATIVE DISCLAIMS ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTY THAT THE USE OF THE INFORMATION HEREIN WILL NOT INFRINGE ANY RIGHTS OR ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE."

