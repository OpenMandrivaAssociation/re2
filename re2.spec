%define major 0
%define libname %mklibname re2_ %{major}
%define develname %mklibname re2 -d
%define oddname %(echo %{version} |sed -e 's,\\.,-,g')
# (tpg) optimize it a bit
%global optflags %{optflags} -O3

Summary:	An efficient, principled regular expression library
Name:		re2
Version:	2019.04.01
Release:	1
License:	BSD like
Group:		System/Libraries
URL:		https://github.com/google/re2/releases
Source0:	https://github.com/google/re2/archive/%{name}-%{oddname}.tar.gz
%description
RE2 is a fast, safe, thread-friendly alternative to backtracking regular
expression engines like those used in PCRE, Perl, and Python.

%package -n %{libname}
Summary:	An efficient, principled regular expression library
Group:		System/Libraries

%description -n %{libname}
RE2 is a fast, safe, thread-friendly alternative to backtracking regular
expression engines like those used in PCRE, Perl, and Python.

%package -n %{develname}
Summary:	Development files for the re2 library
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{develname}
RE2 is a fast, safe, thread-friendly alternative to backtracking regular
expression engines like those used in PCRE, Perl, and Python.

This package contains the development files for re2.

%prep
%autosetup -n re2-%{oddname} -p1

%build
export CXXFLAGS="%{optflags} -pthread -std=c++14"
export LDFLAGS="%{ldflags} -pthread"
%make_build CC=%{__cc} CXX=%{__cxx}

%install
%make_install prefix=%{_prefix} libdir=%{_libdir}
rm -f %{buildroot}%{_libdir}/*.a

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc LICENSE
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/
