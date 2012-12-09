# Copyright (c) 2000-2007, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

Name:           xml-commons-apis12
Version:        1.2.04
Release:        8
Summary:        JAXP 1.2, DOM 2, SAX 2.0.1, SAX2-ext 1.0 apis
Group:          System/Libraries
URL:            http://xml.apache.org/commons/
License:        ASL 2.0 and W3C and Public Domain
Source0:        xml-commons-external-1.2.04.tar.gz
# svn export http://svn.apache.org/repos/asf/xml/commons/tags/xml-commons-external-1_2_04/

Provides:       jaxp = 1.2
Provides:       dom = 2
Provides:       sax = 2.0.1
Provides:       xslt = 1.0

Requires:       jpackage-utils >= 0:1.6

BuildRequires:  ant
BuildRequires:  jpackage-utils >= 0:1.6
BuildArch:      noarch

%description 
DOM 2 org.w3c.dom and SAX XML 2.0 org.xml.sax processor apis used 
by several pieces of Apache software. XSLT 1.0.
This version includes the JAXP 1.2 APIs -- Java API for XML 
Processing 1.2, i.e. javax.xml{.parsers,.transform}

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Provides:       %{name}-apis-javadoc = %{version}-%{release}

%description javadoc
%{summary}.

%package manual
Group:          Development/Java
Summary:        Documents for %{name}

%description manual
%{summary}.

%prep
%setup -q -c

%build
ant -f xml-commons-external-1_2_04/java/external/build.xml jar javadoc

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_javadir}
install -m 644 xml-commons-external-1_2_04/java/external/build/xml-apis.jar \
    %{buildroot}%{_javadir}/%{name}-%{version}.jar

pushd %{buildroot}%{_javadir}
for jar in *-%{version}*; do
ln -sf ${jar} $(echo $jar | sed -e 's|-%{version}\.jar|.jar|');
done

ln -sf %{name}.jar xml-commons-jaxp-1.2-apis.jar
ln -sf %{name}.jar jaxp12.jar
ln -sf %{name}.jar dom2.jar
popd


# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr xml-commons-external-1_2_04/java/external/build/docs/javadoc/* \
    %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
rm -rf xml-commons-external-1_2_04/java/external/build/docs/javadoc

# manuals
install -d -m 755 %{buildroot}%{_docdir}/%{name}-%{version}
cp -pr xml-commons-external-1_2_04/java/external/build/docs/* %{buildroot}%{_docdir}/%{name}-%{version}

%files 
%defattr(0644,root,root,0755)
%{_javadir}/%{name}*.jar
%{_javadir}/jaxp12.jar
%{_javadir}/dom2.jar
%{_javadir}/xml-commons-jaxp-1.2-apis.jar
%doc xml-commons-external-1_2_04/java/external/LICENSE
%doc xml-commons-external-1_2_04/java/external/LICENSE.dom-documentation.txt
%doc xml-commons-external-1_2_04/java/external/LICENSE.dom-software.txt
%doc xml-commons-external-1_2_04/java/external/LICENSE.sax.txt
%doc xml-commons-external-1_2_04/java/external/README.dom.txt
%doc xml-commons-external-1_2_04/java/external/README-sax
%doc xml-commons-external-1_2_04/java/external/README.sax.txt
%doc xml-commons-external-1_2_04/java/external/NOTICE

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%defattr(0644,root,root,0755)
%{_docdir}/%{name}-%{version}

# -----------------------------------------------------------------------------



%changelog
* Fri Jul 13 2012 Guilherme Moro <guilherme@mandriva.com> 1.2.04-8
+ Revision: 809090
- clean up spec

* Sun Nov 27 2011 Guilherme Moro <guilherme@mandriva.com> 1.2.04-7
+ Revision: 734302
- rebuild
- imported package xml-commons-apis12

