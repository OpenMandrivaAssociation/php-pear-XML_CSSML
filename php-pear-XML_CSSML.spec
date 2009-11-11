%define		_class		XML
%define		_subclass	CSSML
%define		upstream_name	%{_class}_%{_subclass}

%define		_requires_exceptions pear(../CSSML.php)

Name:		php-pear-%{upstream_name}
Version:	1.1.1
Release:	%mkrel 5
Summary:	Methods for creating cascading style sheets (CSS)
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/XML_CSSML/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The best way to describe this library is to classify it as a template
system for generating cascading style sheets (CSS). It is ideal for
storing all of the CSS in a single location and allowing it to be
parsed as needed at runtime (or from cache) using both general and
browser filters specified in the attribute for the style tags. It can
be driven with either the libxslt pear extenstion (part of xmldom) or
the xslt extension (part of the sablotron libraries). You may see an
example usage of this class at the follow url:
http://mojave.mojavelinux.com/forum/viewtopic.php?p=22#22

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/%{_class}_%{_subclass}
%{_datadir}/pear/packages/%{upstream_name}.xml


