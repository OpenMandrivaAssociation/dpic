%define _empty_manifest_terminate_build 0

Name:		dpic
Version:	2024.01.01
Release:	1
Summary:	Pic language processor
License:	BSD
Group:		Publishing
URL:		http://www.ece.uwaterloo.ca/~aplevich/dpic/
Source0:	https://ece.uwaterloo.ca/~aplevich/dpic/%{name}-%{version}.tar.gz
BuildRequires:  texlive-latex.bin
BuildRequires:	texlive-mkjobtexmf

%description
Pic language processor for LaTeX documents or web sites.

%files
%doc README CHANGES
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


#--------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure
%make_build
#make_build -C doc

%install
%make_install
#install -d %{buildroot}%{_datadir}/%{name}/doc
install -Dm 644 doc/dpic.1 %{buildroot}%{_mandir}/man1/dpic.1
mv %{buildroot}/bin %{buildroot}%{_prefix}/
#mv %{buildroot}/share/doc/dpic/dpictools.pic %{buildroot}%{_datadir}/%{name}/doc/
rm -rf %{buildroot}/share
