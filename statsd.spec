Summary:	Lightweight network daemon to collect metrics over UDP
Name:		statsd
Version:	0.6.0
Release:	0.5
License:	BSD
Group:		Networking/Daemons
Source0:	https://github.com/etsy/statsd/archive/v0.6.0.tar.gz?/%{name}-%{version}.tgz
# Source0-md5:	56eece3aec5fa9745822d1d34a6e193a
URL:		https://github.com/etsy/statsd
BuildRequires:	sed >= 4.0
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/%{name}

%description
A network daemon that runs on the Node.js platform and listens for
statistics, like counters and timers, sent over UDP and sends
aggregates to one or more pluggable backend services (e.g., Graphite).

%prep
%setup -q
%{__sed} -i -e '1s,^#!.*node,#!/usr/bin/node,' bin/*

%install
rm -rf $RPM_BUILD_ROOT
# install the js files which to the work
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a *.js bin lib backends $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md Changelog.md LICENSE
%dir %{_appdir}
%{_appdir}/stats.js
%{_appdir}/exampleConfig.js
%{_appdir}/backends
%{_appdir}/lib
%dir %{_appdir}/bin
%attr(755,root,root) %{_appdir}/bin/statsd
