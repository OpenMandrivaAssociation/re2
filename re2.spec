%define	major 0
%define	libname %mklibname re2_ %{major}
%define develname %mklibname re2 -d

Summary:	An efficient, principled regular expression library
Name:		re2
Version:	0
Release:	%mkrel 1
License:	BSD like
Group:		System/Libraries
URL:		http://code.google.com/p/re2/
# hg clone https://re2.googlecode.com/hg re2
Source0:	re2.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
RE2 is a fast, safe, thread-friendly alternative to backtracking regular
expression engines like those used in PCRE, Perl, and Python.

%package -n	%{libname}
Summary:	An efficient, principled regular expression library
Group:		System/Libraries

%description -n	%{libname}
RE2 is a fast, safe, thread-friendly alternative to backtracking regular
expression engines like those used in PCRE, Perl, and Python.

%package -n	%{develname}
Summary:	Development files for the re2 library
Group:		Development/C++
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
RE2 is a fast, safe, thread-friendly alternative to backtracking regular
expression engines like those used in PCRE, Perl, and Python.

This package contains the development files for re2.

%prep

%setup -q -n re2

%build

%make CXXFLAGS="%{optflags} -pthread"

%install
rm -rf %{buildroot}

%makeinstall_std prefix=%{_prefix} libdir=%{_libdir}

rm -f %{buildroot}%{_libdir}/*.a

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root,-)
%doc LICENSE
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_includedir}/%{name}/

