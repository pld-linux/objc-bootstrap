Summary:	Portable Object Compiler - bootstrap version
Summary(pl):	Przenaszalny Kompilator Obiektowego C - wersja do inicjacji
Name:		objc-bootstrap
Version:	3.1.33
Release:	1
License:	LGPL
Group:		Development/Tools
Source0:	http://users.pandora.be/stes/%{name}-%{version}.tar.gz
# Source0-md5:	7e02a5ce5e9937c3bfced3a2af640dae
URL:		http://users.pandora.be/stes/compiler.html
BuildRequires:	automake
BuildRequires:	byacc
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Portable Object Compiler consists of a set of Objective-C class
libraries and a precompiler (translator) that generates plain C.
This version is destined only to bootstrap objc compiler.

%description -l pl
Przenaszalny Kompilator Obiektowego C zawiera zbi�r bibliotek
Obiektowego C oraz prekompilator (translator), kt�ry generuje kod
�r�d�owy w czystym C.
Ta wersja jest przeznaczona wy��cznie do inicjacji w�a�ciwego 
kompilatora objc.

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
