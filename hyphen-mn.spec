Name: hyphen-mn
Summary: Mongolian hyphenation rules
%define upstreamid 20090315
Version: 0.%{upstreamid}
Release: 2.1%{?dist}
Source: http://tug.org/svn/texhyphen/trunk/hyph-utf8/tex/generic/hyph-utf8/patterns/hyph-mn-cyrl-x-2a.tex
Group: Applications/Text
URL: http://www.ctan.org/tex-archive/help/Catalogue/entries/mnhyphn.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LPPL
BuildArch: noarch
BuildRequires: hyphen-devel
Requires: hyphen
Patch0: hyphen-mn-cleantex.patch

%description
Mongolian hyphenation rules.

%prep
%setup -T -q -c -n hyphen-mn
cp -p %{SOURCE0} .
%patch0 -p0 -b .clean

%build
substrings.pl hyph-mn-cyrl-x-2a.tex hyph_mn_MN.dic UTF-8
echo "Created with substring.pl by substrings.pl hyph-mn-cyrl-x-2a.tex hyph_mn_MN.dic UTF-8" > README
echo "where hyph-mn-cyrl-x-2a.tex is..." >> README
echo "---" >> README
cat hyph-mn-cyrl-x-2a.tex >> README

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_mn_MN.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{_datadir}/hyphen/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20090315-2.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090315-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Mar 16 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090315-1
- initial version
