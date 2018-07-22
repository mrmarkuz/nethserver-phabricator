Name: nethserver-phabricator
Summary: NethServer phabricator configuration
Version: 0.0.1
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name}

Requires: nethserver-httpd,nethserver-mysql,git

BuildRequires: nethserver-devtools
%description
The %{name} package provides phabricator, a dev portal.

%prep
%setup

%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
(cd root   ; find . -depth -not -name '*.orig' -print  | cpio -dump %{buildroot})
%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%doc COPYING
%doc README.md

%changelog
