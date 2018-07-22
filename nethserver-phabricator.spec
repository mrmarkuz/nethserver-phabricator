Name: nethserver-phabricator
Summary: NethServer phabricator configuration
Version: 3.1.1
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name}

Requires: net-tools
# perl-TimeDate is needed for certificate renew
Requires: nethserver-yum
Requires: nethserver-lib, perl(NethServer::Database::Hostname)

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
