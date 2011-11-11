%define	snap	20100616
Summary:	DVB streaming into individual multicast groups
Name:		getstream
Version:	2.0.%{snap}
Release:	2
License:	GPL v2
Group:		Applications/Networking
Source0:	http://silicon-verl.de/home/flo/projects/streaming/download/%{name}2-%{snap}.tgz
# Source0-md5:	5a3956f77902291cad09d15e5896d99f
URL:		http://silicon-verl.de/home/flo/projects/streaming/
BuildRequires:	glib2-devel
BuildRequires:	libevent-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program allows streaming a full DVB transponder into individual
multicast groups, one per program into the local area network using a
budget card. It's features are:
* full transponder streaming,
* DVB-T/C/S/S2 support (S2 via S2API),
* UDP or RTP multicast streaming,
* SAP/SDP Announcements (VLC Compatible) for multicast streams,
* HTTP streaming for unicast setups,
* High optimization for multiple transponders per machine.

%prep
%setup -q -n %{name}2-%{snap}

%build
%{__make} \
	CFLAGS="-I%{_includedir}/glib-2.0 -I%{_libdir}/glib-2.0/include -Wall %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install getstream tsdecode $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc configs README*
%attr(755,root,root) %{_bindir}/getstream
%attr(755,root,root) %{_bindir}/tsdecode
