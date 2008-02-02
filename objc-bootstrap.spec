Summary:	Portable Object Compiler - bootstrap version
Summary(pl.UTF-8):	Przenośny kompilator obiektowego C - wersja do inicjacji
Name:		objc-bootstrap
Version:	3.2.8
Release:	1
License:	LGPL
Group:		Development/Tools
Source0:	http://users.pandora.be/stes/%{name}-%{version}.tar.gz
# Source0-md5:	cc613d3496fff120c807f8dd4b00110f
URL:		http://users.pandora.be/stes/compiler.html
BuildRequires:	automake
BuildRequires:	byacc
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Portable Object Compiler consists of a set of Objective-C class
libraries and a precompiler (translator) that generates plain C.
This version is destined only to bootstrap objc compiler.

%description -l pl.UTF-8
Przenośny kompilator obiektowego C zawiera zbiór bibliotek obiektowego
C oraz prekompilator (translator), który generuje kod źródłowy w
czystym C. Ta wersja jest przeznaczona wyłącznie do inicjacji
właściwego kompilatora objc.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* util
%configure \
	--with-cplus
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}

%{__make} install \
	INSTALLDIR=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BOOTSTRAP
%attr(755,root,root) %{_bindir}/*
