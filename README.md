Dmomint integration/staging tree
================================
Block explorer:https://explorer.dmoblock.com

Wallet download:https://www.dmoblock.com/#/wallet

Official website:https://www.dmoblock.com

White paper:https://dappdown.oss-cn-hongkong.aliyuncs.com/domino/DOMINO-WHITEPAPER-v1.pdf

Platform mechanism:https://dappdown.oss-cn-hongkong.aliyuncs.com/domino/DMOppt.pdf

One picture fun:https://dappdown.oss-cn-hongkong.aliyuncs.com/domino/DOMINO.jpg

Platform Introduction:https://dappdown.oss-cn-hongkong.aliyuncs.com/domino/DMO.pdf

Community dynamics:https://www.dmoblock.com/#/dynamic?tab=1

Copyright (c) 2018 DmoMintCore Developers

What is Dmomint?
----------------

Dmomint is an experimental new digital currency that enables instant payments to
anyone, anywhere in the world. dmomint uses peer-to-peer technology to operate
with no central authority: managing transactions and issuing money are carried
out collectively by the network. dmomint is also the name of the open source
software which enables the use of this currency.

For more information, as well as an immediately useable, binary version of
the DmoMintCore client software, see https://www.dmoblock.com.

License
-------

DmoMintCore is released under the terms of the GNU GPL v. 3 license. See https://www.gnu.org/licenses/gpl-3.0.en.html for more information.

THIRD PARTY SOFTWARE DISCLOSURE, ATTRIBUTIONS, COPYRIGHT NOTICES, AND LICENSES 

Certain open source third-party software and data components are integrated and/or redistributed with
DmoMintCore. Such third-party components include terms and conditions, such as attribution and liability disclaimers (collectively "Third Party Disclosures") for which disclosure is required by their respective owners. This notice sets forth such Third Party Disclosures for DmoMintCore. 

DMO MINT FOUNDATION MAKES NO REPRESENTATION, WARRANTY OR OTHER COMMITMENT REGARDING SUCH THIRD PARTY COMPONENTS.  DMOMINTCORE, AND ALL THIRD PARTY COMPONENTS, ARE DISTRIBUTED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED, UNLESS PROHIBITED BY APPLICABLE LAW


1. Openssl
•	Copyright (c) 1998-2018 The OpenSSL Project, all rights reserved
•	Copyright (c) 1995-1998 Eric A. Young, Tim J. Hudson, all rights reserved
•	All rights reserved.
•	URL: https://www.openssl.org/
•	Version: 1.1.0g
•	License 1: Original SSLeay License
•	License 2: Apache License 1.0
•	License 3: Apache License 2.0

2. Berkeley DB

•	Copyright (c) 1990, 1993, 1994, 1995	The Regents of the University of California, all rights reserved
•	Copyright (c) 1995, 1996 The President and Fellows of Harvard University, all rights reserved
•	URL: http://www.oracle.com/technetwork/database/database-technologies/berkeleydb/overview/index.html
•	Version: 5.1.29
•	License:  Affero General Public License v.3

3. Level db
•	Copyright (c) 2011 The LevelDB Authors. All rights reserved.
•	URL: http://leveldb.org/
•	Version:1.1
•	License:  BSD License Clause 3

4. Boost 
•	Copyright Beman Dawes, David Abrahams, 1998-2005.
•	Copyright Rene Rivera 2004-2005.
•	URL: https://www.boost.org/
•	Version: 1.65.0
•	License:  Boost Software License

5. libpng 
•	libpng versions 1.0.7, July 1, 2000 through 1.6.32, August 24, 2017 are Copyright (c) 2000-2002, 2004, 2006-2017 Glenn Randers-Pehrson, are derived from libpng-1.0.6, and are distributed according to the same disclaimer and license as libpng-1.0.6 with the following individuals added to the list of Contributing Authors:

o	   Simon-Pierre Cadieux
o	   Eric S. Raymond
o	   Mans Rullgard
o	   Cosmin Truta
o	   Gilles Vollant
o	   James Yu
o	   Mandar Sahastrabuddhe
o	   Google Inc.
o	   Vadim Barkov
•	URL: http://libpng.org/
•	Version: 1.6.16
•	License: libpng license

6. Protocol buffer
•	Copyright 2008 Google, Inc.
•	URL: https://developers.google.com/protocol-buffers/
•	Version: 2.6.1
•	License: BSD

7. qrencode
•	Copyright 2006-2017 Kentaro Fukuchi kentaro@fukuchi.org.
•	URL: https://fukuchi.org/works/qrencode/manual/index.html
•	Version: 3.4.4
•	License:  GNU Lesser General Public License 2.1

8. Qt
•	Copyright Various Years, QT Company
•	URL: www.qt.io
•	Version: 5.6.3
•	License GPL v. 2; GPL v. 3; : LGPL v. 3


9. Google Test
•	Copyright 2008, Google Inc., all rights reserved
•	URL: https://github.com/google/googletest/
•	Version: 
•	License BSD 3-Clause

10. MiniUPnP
•	Copyright (c) 2006-2017, Thomas BERNARD, all rights reserved
•	URL:http://miniupnp.free.fr/
•	Version: 2.1
•	License: MiniUPnP License

11. Bitcoin Core
•	Copyright (c) 2009-2018 The Bitcoin Core developers
•	URL:https://bitcoin.org/en/bitcoin-core/
•	Version:0.8.6
•	License: MIT License

12. libFES algorithm
•	URL: http://www.lifl.fr/~bouillag/fes/index.html
•	Version:0.2
•	GPL V3



Development process
-------------------

Developers work in their own trees, then submit pull requests when they think
their feature or bug fix is ready.

If it is a simple/trivial/non-controversial change, then one of the DmoMintCore
development team members simply pulls it.

If it is a *more complicated or potentially controversial* change, then the patch
submitter will be asked to start a discussion (if they haven't already) on the
[mailing list](http://sourceforge.net/mailarchive/forum.php?forum_name=dmomint-development).

The patch will be accepted if there is broad consensus that it is a good thing.
Developers should expect to rework and resubmit patches if the code doesn't
match the project's coding conventions (see `doc/coding.md`) or are
controversial.

The `master` branch is regularly built and tested, but is not guaranteed to be
completely stable. [Tags](https://github.com/dmomint/dmomint/tags) are created
regularly to indicate new official, stable release versions of dmomint.

Testing
-------

Testing and code review is the bottleneck for development; we get more pull
requests than we can review and test. Please be patient and help out, and
remember this is a security-critical project where any mistake might cost people
lots of money.

### Automated Testing

Developers are strongly encouraged to write unit tests for new code, and to
submit new unit tests for old code.

Unit tests for the core code are in `src/test/`. To compile and run them:

    cd src; make -f makefile.unix test

Unit tests for the GUI code are in `src/qt/test/`. To compile and run them:

    qmake DMOMINT_QT_TEST=1 -o Makefile.test dmomint-qt.pro
    make -f Makefile.test
    ./dmomint-qt_test

Every pull request is built for both Windows and Linux on a dedicated server,
and unit and sanity tests are automatically run. The binaries produced may be
used for manual QA testing — a link to them will appear in a comment on the
pull request posted by [dmomintPullTester](https://github.com/dmomintPullTester). See https://github.com/TheBlueMatt/test-scripts
for the build/test scripts.

### Manual Quality Assurance (QA) Testing

Large changes should have a test plan, and should be tested by somebody other
than the developer who wrote the code.

See https://github.com/dmomint/QA/ for how to create a test plan.

### Mining Algorithm Using GPU 
A new program that can be used to do dmo mining on a GPU is recently release at
http://polycephaly.org/projects/forcemq/data/MQForceGPU-20180724.tgz

To use it correctly, one may have to do some small adjustments. 

About Falcon
Falcon is a cryptographic signature algorithm submitted to NIST Post-Quantum Cryptography Project on November 30th, 2017. It has been designed by: Pierre-Alain Fouque, Jeffrey Hoffstein, Paul Kirchner, Vadim Lyubashevsky, Thomas Pornin, Thomas Prest, Thomas Ricosset, Gregor Seiler, William Whyte, Zhenfei Zhang.

The point of a post-quantum cryptographic algorithm is to keep on ensuring its security characteristics even faced with quantum computers. Quantum computers are deemed feasible, according to our current understanding of the laws of physics, but some significant technological issues remain to be solved in order to build a fully operational unit. Such a quantum computer would very efficiently break the usual asymmetric encryption and digitial signature algorithms based on number theory (RSA, DSA, Diffie-Hellman, ElGamal, and their elliptic curve variants).

Falcon is based on the theoretical framework of Gentry, Peikert and Vaikuntanathan for lattice-based signature schemes. We instantiate that framework over NTRU lattices, with a trapdoor sampler called "fast Fourier sampling". The underlying hard problem is the short integer solution problem (SIS) over NTRU lattices, for which no efficient solving algorithm is currently known in the general case, even with the help of quantum computers.

Algorithm Highlights
Falcon offers the following features:

Security: a true Gaussian sampler is used internally, which guarantees negligible leakage of information on the secret key up to a practically infinite number of signatures (more than 264).
Compactness: thanks to the use of NTRU lattices, signatures are substantially shorter than in any lattice-based signature scheme with the same security guarantees, while the public keys are around the same size.
Speed: use of fast Fourier sampling allows for very fast implementations, in the thousands of signatures per second on a common computer; verification is five to ten times faster.
Scalability: operations have cost O(n log n) for degree n, allowing the use of very long-term security parameters at moderate cost.
RAM Economy: the enhanced key generation algorithm of Falcon uses less than 30 kilobytes of RAM, a hundredfold improvement over previous designs such as NTRUSign. Falcon is compatible with small, memory-constrained embedded devices.
Performance
While resistance to quantum computers is the main drive for the design and development of Falcon, the algorithm may achieve significant adoption only if it is also reasonably efficient in our current world, where quantum computers do not really exist. Using the reference implementation on a common desktop computer (Intel® Core® i5-8259U at 2.3 GHz, TurboBoost disabled), Falcon achieves the following performance:

variant	keygen (ms)	keygen (RAM)	sign/s	verify/s	pub size	sig size
Falcon-512	8.64	14336	5948.1	27933.0	897	666
Falcon-1024	27.45	28672	2913.0	13650.0	1793	1280
Sizes (key generation RAM usage, public key size, signature size) are expressed in bytes. Key generation time is given in milliseconds. Private key size (not listed above) is about three times that of a signature, and it could be theoretically compressed down to a small PRNG seed (say, 32 bytes), if the signer accepts to run the key generation algorithm every time the key must be loaded.

To give a point of comparison, Falcon-512 is roughly equivalent, in classical security terms, to RSA-2048, whose signatures and public keys use 256 bytes each. On the specific system on which these measures were taken, OpenSSL's thoroughly optimized assembly implementation achieves about 1140 signatures per second; thus, Falcon's reference implementation, which is portable and uses no inline assembly on x86 CPUs, is already more than five times faster, and it scales better to larger sizes (for long-term security).

Resources
Falcon submission package [zip] (specification, source code, scripts and test vectors)
Falcon specification [pdf]
Falcon reference implementation:
Source code archive [zip]
Browse source code online [html]
An implementation in Python [html]
For reference, submission packages for previous rounds: Round 1 [zip] and Round 2 [zip]
Presentations at the NIST PQC Standardization Conferences: Round 1 [pdf] and Round 2 [pdf]
Related works
Thomas Pornin and Thomas Prest
More Efficient Algorithms for the NTRU Key Generation using the Field Norm [pdf]
Xingye Lu, Man Ho Au and Zhenfei Zhang
Raptor: A Practical Lattice-Based (Linkable) Ring Signature [pdf]
Thomas Pornin
New Efficient, Constant-Time Implementations of Falcon [pdf]
Pierre-Alain Fouque, Paul Kirchner, Mehdi Tibouchi, Alexandre Wallet and Yang Yu
Key Recovery from Gram-Schmidt Norm Leakage in Hash-and-Sign Signatures over NTRU Lattices [pdf]
James Howe, Thomas Prest, Thomas Ricosset and Mélissa Rossi
Isochronous Gaussian Sampling: From Inception to Implementation [pdf]
