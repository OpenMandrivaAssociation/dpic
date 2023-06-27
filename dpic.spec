Name:		dpic
Version:	2023.06.01
Release:	1
Summary:	Pic language processor
License:	BSD
Group:		Publishing
URL:		http://www.ece.uwaterloo.ca/~aplevich/dpic/
Source0:	https://ece.uwaterloo.ca/~aplevich/dpic/%{name}-%{version}.tar.gz

%description
Pic language processor for LaTeX documents or web sites.

%files
%doc README CHANGES doc/dpicdoc.pdf
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


#--------------------------------------------------------------------

%prep
%autosetup -p1

%build
%setup_compile_flags
%make

%install
install -Dm 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm 0644 doc/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

